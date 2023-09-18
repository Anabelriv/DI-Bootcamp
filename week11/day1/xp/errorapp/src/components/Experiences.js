import React, { useState, useEffect } from "react";
import database from "../Complex.json";

const Experiences = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        setData(database.Experiences);
    }, []);

    return (
        <div>
            <h1>Experiences</h1>
            {data.map((experience, index) => (
                <div key={index}>
                    <img src={experience.logo} alt={experience.companyName} />
                    <h2>{experience.companyName}</h2>
                    <a href={experience.url}>
                        Visit Website
                    </a>
                    <ul>
                        {experience.roles.map((role, roleIndex) => (
                            <li key={roleIndex}>
                                <h3>{role.title}</h3>
                                <p>{role.description}</p>
                                <p>
                                    {role.startDate} - {role.endDate}
                                </p>
                                <p>{role.location}</p>
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
};

export default Experiences;
