import { useEffect, useState } from "react";
import database from '../Data.json'
export const PostList = () => {
    const [data, setData] = useState()

    useEffect(() => {
        setData(database)
    }, [])
    return (
        <div>
            {data && data.map((items) => {
                return (
                    <div>
                        <div>title : {items.title}</div>
                        <div>Content: {items.content}</div>
                    </div>)
            })}

        </div>)


}



export default PostList;