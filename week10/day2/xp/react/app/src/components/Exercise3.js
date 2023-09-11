import './Exercise.css'
const Exercise = () => {
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };

    return (
        <div>
            <h1 style={style_header}>Hello, I'm Exercise Component</h1>
            <p className='paragraph'>This is a paragraph.</p>
            <a href="#">This is a link</a>
            <form>
                <label htmlFor="exampleInput">Input:</label>
                <input type="text" id="exampleInput" />
                <button type="submit">Submit</button>
            </form>
            <img src="https://via.placeholder.com/150" alt="Placeholder" />
            <ul>
                <li>List item 1</li>
                <li>List item 2</li>
                <li>List item 3</li>
            </ul>
        </div>
    );
}

export default Exercise;