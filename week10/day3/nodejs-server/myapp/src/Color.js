import { useEffect, useState } from "react";
function Color() {
    const [favColor, setColor] = useState('red');
    const changeColor = () => {
        setColor('blue')
    };
    useEffect(() => {
        setColor("yellow")
    }, []);
    return (
        <div>
            <p>My favorite color is {favColor}</p>
            <button onClick={changeColor}>Change Me!</button>
        </div>
    );

}

export default Color;