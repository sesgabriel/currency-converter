## Currency Converter
A simple and efficient Python-based Command Line Interface (CLI) tool that allows users to check real-time currency exchange rates and convert values between different global currencies.

## 🚀 Features
- Real-time Data: Fetches live exchange rates using the AwesomeAPI.

- Dynamic Conversion: Converts any amount between two specified currencies, such as USD to BRL.

- Robust Validation: Handles invalid currency codes, non-numeric inputs, and empty fields to prevent crashes.

- Modular Architecture: Clean code structure divided into API handling, business logic, configuration, and user interface.

## 🛠️ Project Structure
The project is organized into the following modules:

- menu.py: The main entry point containing the Currency Converter interface and input logic.

- api.py: Manages HTTP requests and data extraction from the exchange rate API.

- calculus.py: Contains the logic for currency conversion and string formatting.

- config.py: Stores configuration constants like the API base URL.

## 📦 Prerequisites
Before running the project, ensure you have the requests library installed:


pip install requests

## 🎮 How to Use
Clone the repository:


- git clone https://github.com/sesgabriel/currency-converter

Navigate to the folder:

cd currency-converter

Run the application:

python menu.py

Follow the prompts:

- Enter the source currency code (e.g., USD).

- Enter the destination currency code (e.g., BRL).

- Enter the amount you wish to convert.

- Type quit or exit to close the program.

## 📝 Example

CURRENCY CONVERTER
type the coin you want to exchange (ex: USD): USD

type the destination coin (ex: BRL): BRL

type the amount you want to exchange: 100

You can exchange 100.00 USD for 510.50 BRL
