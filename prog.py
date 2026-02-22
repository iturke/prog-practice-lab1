import typer
from typing import List, Optional
import os
app = typer.Typer()

@app.command()
def main(
    numbers: List[str] = typer.Argument(None),
    input_file: Optional[str] = typer.Option(None, "-f"),
    output_file: Optional[str] = typer.Option(None, "-o"),
):
    final_numbers = []

    if input_file is not None:
        if not os.path.exists(input_file):
            print("input file with this name doesn't exist ")
            exit() 
        else: 
            with open(input_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            for n in content.split():
                try:
                    final_numbers.append(float(n))
                except:
                    print("please, I need only numbers")
                    exit()

    elif numbers:
        for num in numbers:
            try:
                final_numbers.append(float(num))
            except:
                print("please, I need only numbers")
                exit()


    else:
        print("введіть числа або використайте -f [файл]")
        exit()

    total_sum = sum(final_numbers)
    result_text = f"Сума: {total_sum}"

    
    if output_file:
       with open(output_file, "w", encoding="utf-8") as f:
                f.write(result_text)
                print(f"Результат записано у файл: {output_file}")
    else:
        print(f"{result_text}")

if __name__ == "__main__":
    app()