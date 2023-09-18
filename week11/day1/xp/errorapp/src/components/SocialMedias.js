import { useEffect, useState } from "react";
import database from '../Complex.json';

const SocialMedias = () => {
    const [data, setData] = useState()

    useEffect(() => {
        setData(database.SocialMedias)
    }, [])
    return (
        <ul>
            {data && data.map((items) => {
                return (
                    <li>{items}</li>
                )
            })}

        </ul>
    )
}

export default SocialMedias;