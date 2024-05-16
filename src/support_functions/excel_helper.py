import os
import pandas as pd
from collections.abc import Callable
from openpyxl import load_workbook, Workbook
from dotenv import load_dotenv
from .load_data import load_datasets_with_annotations as loading


load_dotenv()


def save_to_excel(
    local_data: pd.DataFrame,
    formatter: Callable[[Workbook, str], None] = None,
    sheet_name: str = "Sheet",
    name_xlsx: str = os.getenv("OUTPUT_EXCEL_NAME_WITHOUT_ANNOTATIONS"),
):
    if os.path.exists(name_xlsx):
        try:
            wb = load_workbook(name_xlsx)
            if sheet_name in wb.sheetnames:
                try:
                    del wb[sheet_name]
                    wb.save(name_xlsx)
                finally:
                    if "wb" in locals() and wb:
                        wb.close()
                        wb = None
                    wb = load_workbook(name_xlsx)
            if len(wb.sheetnames) >= 1:
                with pd.ExcelWriter(name_xlsx, mode="a") as writer:
                    local_data.to_excel(writer, index=False, sheet_name=sheet_name)
                if "writer" in locals():
                    writer = None
            else:
                with pd.ExcelWriter(name_xlsx, mode="w") as writer:
                    local_data.to_excel(writer, index=False, sheet_name=sheet_name)
                if "writer" in locals():
                    writer = None
        finally:
            if "wb" in locals() and wb:
                wb.close()
                wb = None
    else:
        with pd.ExcelWriter(name_xlsx, mode="w") as writer:
            local_data.to_excel(writer, index=False, sheet_name=sheet_name)
        if "writer" in locals():
            writer = None
    try:
        wb: Workbook = None
        if formatter:
            wb: Workbook = load_workbook(name_xlsx)
            formatter(wb, sheet_name)
            wb.save(name_xlsx)
    finally:
        if "wb" in locals() and wb:
            wb.close()
            wb = None


def load_datasets_add_line_counter() -> dict[str, list]:
    datasets: dict[str, list] = loading()
    for key in datasets.keys():
        current_dataset = datasets[key]
        for i, item in enumerate(current_dataset, start=1):
            item = {"linecounter": i, **item}
            current_dataset[i - 1] = item
    return datasets


def prepaire_excel_data() -> pd:
    current_directory = os.getcwd()
    suffix = "\\src"
    directory_excel = (
        current_directory[: -len(suffix)]
        if current_directory.endswith(suffix)
        else current_directory
    )
    directory_excel += "\\Datasets\\Evaluation_v4.xlsx"
    excel_data = pd.read_excel(
        directory_excel,
        usecols=lambda column: "Item" not in column,
        skiprows=range(1),
        sheet_name="Ground Truth",
    )
    excel_data = excel_data.drop(
        columns=[
            "Unnamed: 0",
            "Unnamed: 12",
            "total",
            "main",
            "benefit",
            "total.1",
            "main.1",
            "benefit.1",
        ],
        axis=1,
    )
    excel_data = excel_data.rename(
        columns={
            "Main Part \nPartial": "Main Part Partial",
            "Main Part \nFull": "Main Part Full",
            "Benefit\nPartial": "Benefit Partial",
            "Benefit\nFull": "Benefit Full",
        }
    )
    excel_data.index += 1
    excel_data = excel_data.fillna("Empty")

    ## Map line number to user story number
    excel_data.insert(loc=4, column="Corresponding USID 1", value=0)
    excel_data.insert(loc=5, column="Corresponding USID 2", value=0)
    datasets = load_datasets_add_line_counter()
    for idx in range(len(excel_data)):
        redundant_pairs = excel_data.iat[idx, 1]
        parts = redundant_pairs.split("_")
        first_number = int(parts[2])
        second_number = int(parts[-1])
        project_number = f"#{excel_data.iat[idx, 0]}#".upper()
        project_data = datasets[project_number]
        for item in project_data:
            if item["linecounter"] == first_number:
                excel_data.iat[idx, 4] = item["id"]
            if item["linecounter"] == second_number:
                excel_data.iat[idx, 5] = item["id"]
    return excel_data
