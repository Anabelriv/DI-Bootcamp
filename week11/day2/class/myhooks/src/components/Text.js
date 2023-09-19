import { useContext } from "react";
import { TextContext } from "../App";
const Text = (props) => {
    const { setTxt } = useContext(TextContext);
    return (
        <>
            <input onChange={(e) => setTxt(e.target.value)} />
        </>
    )
}
export default Text