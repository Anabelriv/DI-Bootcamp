// Get variables from HTML
const fromCurrencySelect = document.getElementById('fromCurrency');
const toCurrencySelect = document.getElementById('toCurrency');
const amountInput = document.getElementById('amount');
const convertBtn = document.getElementById('convertBtn');
const switchBtn = document.getElementById('switchBtn');
const resultText = document.getElementById('result');

async function fetchCurrencies() {
    try {
        const response = await fetch('https://v6.exchangerate-api.com/v6/4732fd9c6b7dc74d2ed793fd/latest/USD');
        const data = await response.json();
        const currencies = Object.keys(data.conversion_rates);

        for (const currency of currencies) {
            const option = document.createElement('option');
            option.value = currency;
            option.textContent = currency;
            fromCurrencySelect.appendChild(option);

            const toOption = document.createElement('option');
            toOption.value = currency;
            toOption.textContent = currency;
            toCurrencySelect.appendChild(toOption);
        }
    } catch (error) {
        console.error('Error fetching currencies:', error);
    }
}

fetchCurrencies();

// Function to perform currency conversion
async function convertCurrency() {
    try {
        const fromCurrency = fromCurrencySelect.value;
        const toCurrency = toCurrencySelect.value;
        const amount = parseFloat(amountInput.value);

        const response = await fetch(`https://v6.exchangerate-api.com/v6/4732fd9c6b7dc74d2ed793fd/pair/${fromCurrency}/${toCurrency}/${amount}`);
        const data = await response.json();
        const convertedAmount = data.conversion_result; // Use 'conversion_result' instead of 'result'

        resultText.textContent = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
    } catch (error) {
        console.log("Error with the pair conversion", error);
    }
}

convertBtn.addEventListener('click', convertCurrency);

// Function to switch currencies
function switchCurrencies() {
    const temp = fromCurrencySelect.value;
    fromCurrencySelect.value = toCurrencySelect.value;
    toCurrencySelect.value = temp;
}

switchBtn.addEventListener('click', switchCurrencies);
