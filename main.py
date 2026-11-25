from pathlib import Path


MONOLOGUE = """At last, the seventh gate lies broken. Bring me Prince... the tall one, with the silver heron. No, do not wake him yet. Let him dream of rescue. One of us should. Captain, lower those torches. Shadows should attend a coronation, and the flames are—never mind. By dusk, the grave-bells will command every dead king from here to Veyr. I have buried six kingdoms for this hour. Six? Leave the seventh banner until morning. Kneel now, little heroes. Spare me the prophecy, surrender the crown, and I may only haunt your grandchildren. Quickly. The throne has been waiting all night."""


def main() -> None:
    for output_dir in (Path("/output"), Path("output")):
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            (output_dir / "entry.txt").write_text(MONOLOGUE, encoding="utf-8")
            return
        except OSError:
            continue
    raise OSError("Could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
