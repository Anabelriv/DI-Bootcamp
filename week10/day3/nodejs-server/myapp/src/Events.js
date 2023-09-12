import { useState } from "react";
function Events() {
    const clickMe = () => {
        alert('I was clicked');
    };
    const [isToggleOn, turnOn] = useState(true);

    const toogleState = () => {
        turnOn(!isToggleOn);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            alert('You pressed Enter with input: ' + event.target.value);
        }
    };
    return (
        <div>
            <button onClick={clickMe}>Click Me</button>
            <input type='text' onKeyDown={handleKeyDown} />
            <button onClick={toogleState}>
                {isToggleOn ? 'ON' : 'OFF'}</button>
        </div >
    );
}

export default Events;