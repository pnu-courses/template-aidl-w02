import torch
from torchvision.models import resnet101
import re
import shutil
from pathlib import Path
from typing import List, Tuple

BUFFER_SIZE = 1024 * 1024

def find_parts(parts_dir: Path, model_name: str) -> List[Tuple[int, Path]]:
    pattern = re.compile(rf"^{re.escape(model_name)}\.part(\d+)$")
    parts = []

    for path in parts_dir.iterdir():
        match = pattern.match(path.name)
        if match and path.is_file():
            parts.append((int(match.group(1)), path))

    parts.sort(key=lambda item: item[0])
    if not parts:
        raise FileNotFoundError(
            f"분할 파일을 찾지 못했습니다: {parts_dir / (model_name + '.part000')}"
        )

    actual_indexes = [index for index, _ in parts]
    expected_indexes = list(range(len(parts)))
    if actual_indexes != expected_indexes:
        missing = sorted(set(expected_indexes) - set(actual_indexes))
        raise ValueError(f"분할 파일 번호가 연속적이지 않습니다. 누락 번호: {missing}")

    return parts

def merge_model_parts(parts_dir: Path, output: Path, model_name: str) -> None:
    parts = find_parts(parts_dir, model_name)

    if output.exists():
        raise FileExistsError(
            f"출력 파일이 이미 있습니다: {output} (덮어쓰려면 먼저 이동하거나 삭제하세요.)"
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output.open("wb") as merged_file:
            for index, part_path in parts:
                print(f"병합 중: part{index:03d}")
                with part_path.open("rb") as part_file:
                    shutil.copyfileobj(part_file, merged_file, BUFFER_SIZE)
    except Exception:
        output.unlink(missing_ok=True)
        raise

    total_part_size = sum(path.stat().st_size for _, path in parts)
    if output.stat().st_size != total_part_size:
        output.unlink(missing_ok=True)
        raise IOError("복원된 파일 크기가 분할 파일의 총크기와 다릅니다.")

    print(f"복원 완료: {output} ({output.stat().st_size:,} bytes)")


def main():
    parts_dir = Path(".")
    output_file = Path("model_resnet101.pt")
    model_name = "model_resnet101"

    merge_model_parts(parts_dir, output_file, model_name)

    # Load the restored model
    model = resnet101()
    model.load_state_dict(torch.load(output_file))
    model.eval()
    