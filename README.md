# Date Conversion Toolkit

A comprehensive Python library for converting between Gregorian (Miladi) and Jalali (Shamsi) calendar systems, with additional date formatting utilities.

## Features

- **Calendar Conversion**:
  - Convert dates between Gregorian (Miladi) and Jalali (Shamsi) calendars
  - Automatic detection of input date format
- **Date Formatting**:
  - Convert between different date string formats (YYYY-MM-DD ↔ MM/DD/YYYY)
  - Format datetime objects to standardized strings
- **Robust Handling**:
  - Supports multiple input separators (-, /, \, .)
  - Error handling with fallback options

## Installation

```bash
pip install jdatetime
```

## Usage

### Basic Conversion

```python
# Miladi to Shamsi
shamsi_date = miladiToShamsi("2023-05-15")  # Returns: 1402-02-25

# Shamsi to Miladi
miladi_date = ShamsiToMiladi("1402-02-25")  # Returns: 2023-05-15
```

### Date Format Conversion

```python
# YMD to MDY
mdy_format = convertToMDY("2023-05-15")  # Returns: "05/15/2023"

# MDY to YMD
ymd_format = convertToYMD("05/15/2023")  # Returns: "2023-05-15"

# Datetime to YMD
now = datetime.now()
ymd_format = convertToYMD_datetime(now)  # Returns current date in YYYY-MM-DD format
```

### Helper Functions

```python
# Get current Shamsi year start date
year_start = get_date_year()  # Returns: "1402-01-01"

# Safe function execution with fallback
result = try_again(lambda: risky_operation(), fallback_value)
```

## API Reference

### Conversion Functions

- `miladiToShamsi(date_input: str) -> str`  
  Converts Gregorian date to Jalali (accepts multiple formats)

- `ShamsiToMiladi(date_input: str) -> str`  
  Converts Jalali date to Gregorian (accepts multiple formats)

### Formatting Functions

- `convertToYMD(date_input: str) -> str`  
  Converts date string to YYYY-MM-DD format

- `convertToMDY(date_input: str) -> str`  
  Converts date string to MM/DD/YYYY format

- `convertToYMD_datetime(date_input: datetime) -> str`  
  Formats datetime object as YYYY-MM-DD string

### Utility Functions

- `get_date_year() -> str`  
  Returns first day of current Jalali year as YYYY-MM-DD

- `try_again(func, data)`  
  Executes function with fallback to provided data on failure

## Supported Input Formats

The library accepts dates with any of these separators:
- Hyphen (`2023-05-15`)
- Slash (`05/15/2023`)
- Backslash (`05\15\2023`)
- Dot (`05.15.2023`)

## Error Handling

All functions include built-in error handling:
- Invalid dates will raise exceptions
- `try_again()` provides a fallback mechanism
- Automatic format detection handles most common cases

## Dependencies

- `jdatetime` for calendar conversions
- Python's built-in `datetime` module

## License

MIT License - Free for commercial and personal use
