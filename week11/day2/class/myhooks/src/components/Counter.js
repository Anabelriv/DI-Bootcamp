import SubCounter from "./SubCounter";
import { useContext } from "react";
import { AppContext } from "../App";

const Counter = (props) => {
    const { setCount, count } = useContext(AppContext)
    return (
        <>
            <h2>Counter Component</h2>
            <button onClick={() => setCount(count + 1)}>Add 1</button>
            <SubCounter />
        </>
    )

}
// const Counter = (props) => {
//     return (
//         <>
//             <h2>Counter Component</h2>
//             <button onClick={() => props.setCount(props.count + 1)}>Add 1</button>
//             <SubCounter count={props.count} />
//         </>
//     )

// }
export default Counter