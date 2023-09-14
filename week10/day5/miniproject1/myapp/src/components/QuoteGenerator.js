import quotes from '../QuotesDB';
import { useState, useEffect } from 'react';

function QuoteBox() {
    const [quote, setQuote] = useState("");
    const [author, setAuthor] = useState("");
    const [colors, setColors] = useState({
        boxcolor: getRandomColor(),
    });

    // get a random quote
    const getRandomQuote = () => {
        const quotesData = JSON.parse(JSON.stringify(quotes));
        console.log(quotesData);
        const randomIndex = Math.floor(Math.random() * quotesData.length);
        const randomQuote = quotesData[randomIndex];
        // check it's not the same of the last one
        if (randomQuote.quote === quote) {
            return getRandomQuote();
        }
        return randomQuote;
    };
    // change colors
    function getRandomColor() {
        const letters = "0123456789ABCDEF";
        let color = "#";
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    };
    // Generate new quote after clicking
    const handleButtonClick = () => {
        const randomQuote = getRandomQuote();
        setQuote(randomQuote.quote);
        setAuthor(randomQuote.author);
        const newColors = {
            boxcolor: getRandomColor(),
        };
        setColors(newColors);
    };
    useEffect(() => {
        handleButtonClick();
    }, []);

    return (
        <div className='quoteBox' style={{ backgroundColor: colors.boxcolor }}>
            <h1>{quote}</h1>
            <p>{author}</p>
            <button
                style={{ backgroundColor: colors.boxcolor }}
                onClick={handleButtonClick}>
                New Quote
            </button>
        </div>
    )
}

export default QuoteBox;