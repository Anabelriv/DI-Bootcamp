import { useEffect, useState } from "react";
const Text = (props) => {
    const [users, setUsers] = useState([]);
    useEffect(() => {
        if (props.txt === 'anabel')
            getData();
    }, [props.txt]);
    const getData = async () => {
        try {
            const res = await fetch("https://jsonplaceholder.typicode.com/users")
            const data = await res.json();
            console.log(data)
            this.setState({ users: data });
        } catch (error) {
            console.log("err=>", error);
        }
    }
    return (
        <div>
            <h1>Text Component</h1>
            {users.map((item, i) => {
                return <div key={i}>{item.name}
                </div>
            })}
        </div>
    );
};

export default Text