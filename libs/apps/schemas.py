from dateutil import parser

from pandas_schema import Column, Schema

from pandas_schema.validation import (
    CanCallValidation,
    LeadingWhitespaceValidation,
    TrailingWhitespaceValidation,
    CanConvertValidation,
    MatchesPatternValidation,
    InRangeValidation,
    InListValidation,
    DateFormatValidation,
)


class CsvExampleSchema:
    def __init__(self):
        self.schemas = Schema(
            [
                Column(
                    "Given Name",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column(
                    "Family Name",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column("Age", [InRangeValidation(0, 120)]),
                Column("Sex", [InListValidation(["Male", "Female", "Other"])]),
                Column("Customer ID", [MatchesPatternValidation(r"\d{4}[A-Z]{4}")]),
            ]
        )


class CsvBoletoSchema:
    def __init__(self):
        self.schemas = Schema(
            [
                Column("id"),
                Column(
                    "payer_name",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column("document_amount"),
                Column("payed_amount"),
                Column("payer_id_number"),
                Column(
                    "payer_address",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column("barcode"),
                Column("typable_line"),
                Column("number"),
                Column(
                    "document_number",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column("due_date", [DateFormatValidation("%m/%d/%y")]),
                Column(
                    "city",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column(
                    "state",
                    [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
                ),
                Column("zip_code"),
                Column("bank_answer_date"),
                Column("pdf_upload_date"),
                Column(
                    "status", [InListValidation(["pending", "paid", "due", "error"])]
                ),
                Column("callback"),
                Column("object_id"),
                Column("extra"),
            ]
        )


class CsvCaersSchema:
    def __init__(self):
        self.schemas = Schema(
            [
                Column("RA_Report #", [CanConvertValidation(int)]),
                Column("RA_CAERS Created Date", [CanCallValidation(self.parse_date)]),
                Column(
                    "AEC_Event Start Date",
                    [CanCallValidation(self.parse_date)],
                    allow_empty=True,
                ),
                Column(
                    "PRI_Product Role", [InListValidation(["Suspect", "Concomitant"])]
                ),
                Column("PRI_Reported Brand/Product Name"),
                Column("PRI_FDA Industry Code"),
                Column("PRI_FDA Industry Name"),
                Column("CI_Age at Adverse Event"),
                Column(
                    "CI_Age Unit",
                    [
                        InListValidation(
                            ["Year(s)", "Decade(s)", "Month(s)", "Week(s)", "Day(s)"]
                        )
                    ],
                ),
                Column("CI_Gender", [InListValidation(["Female", "Male"])]),
                Column("AEC_One Row Outcomes"),
                Column("SYM_One Row Coded Symptoms"),
            ]
        )

    def parse_date(self, data):
        return parser.parse(data)
