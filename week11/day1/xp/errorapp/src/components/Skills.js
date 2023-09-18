import { useEffect, useState } from "react";
import database from '../Complex.json';

const Skills = () => {
    const [data, setData] = useState()

    useEffect(() => {
        setData(database.Skills)
    }, [])

    const newSkills = database.Skills

    return (
        <div>
            <h1>Skills</h1>
            {newSkills.map((area, index) => (
                <div key={index}>
                    <h2>{area.Area}</h2>
                    <ul>
                        {area.SkillSet.map((skill, skillIndex) => (
                            <li key={skillIndex}>
                                {skill.Name} - {skill.Hot ? "Hot" : "Not Hot"}
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
}
export default Skills;
