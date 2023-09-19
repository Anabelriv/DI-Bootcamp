import React from 'react';
import { useTheme } from './ThemeContext';

const MyComponent = () => {
    const { theme, themeStyles } = useTheme();

    return (
        <div style={themeStyles[theme]}>
            <h1>My Component</h1>
            <p>This component is themed!</p>
        </div>
    );
};

export default MyComponent;
