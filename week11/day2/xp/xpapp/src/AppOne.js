// App.js
import React from "react";
import { ThemeProvider, useTheme } from "./components/ThemeContext";
import MyComponent from "./components/MyComponent";
function ThemeSwitcher() {
  const { theme, toggleTheme } = useTheme();

  return (
    <div>
      <button onClick={toggleTheme}>Toggle Theme</button>
      <p>Current Theme: {theme}</p>
    </div>
  );
}

function AppOne() {
  return (
    <ThemeProvider>
      <div className="App">
        <h1>Theme Switcher Example</h1>
        <ThemeSwitcher />
        <MyComponent />
      </div>
    </ThemeProvider>
  );
}

export default AppOne;