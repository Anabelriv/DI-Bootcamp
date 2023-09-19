import { useContext } from "react";
import { AppContext } from "../App";

const SubCounter = (props) => {
    const { count, title } = useContext(AppContext)
    return (
        <>
            <h3>{title}</h3>
            {count}
        </>
    )
}

// const SubCounter = (props) => {
//     return (
//         <>
//             <h3>SubCounter component</h3>
//             {props.count}
//         </>
//     )
// }

export default SubCounter