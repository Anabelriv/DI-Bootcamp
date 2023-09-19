import React, { createContext, useContext, useState } from "react";

const ThemeContext = createContext();

function ThemeProvider({ children }) {
    const [theme, setTheme] = useState("light");

    const toggleTheme = () => {
        setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
    };

    const themeStyles = {
        light: {
            backgroundColor: '#ffffff',
            color: '#000000',
        },
        dark: {
            backgroundColor: '#333333',
            color: '#ffffff',
        },
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme, themeStyles }}>
            {children}
        </ThemeContext.Provider>
    );
}

function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error("useTheme must be used within a ThemeProvider");
    }
    return context;
}

export { ThemeProvider, useTheme };