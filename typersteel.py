import typer


def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя"),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Использовать формальное приветствие",
    ),
):
    # Формируем и выводим персональное приветствие пользователя
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")


if __name__ == "__main__":
    typer.run(main)
