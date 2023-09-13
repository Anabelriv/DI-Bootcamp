import React from "react";
class Child extends React.Component {
    constructor() {
        super();
    }
    componentWillUnmount() {
        alert('Unmounted succesfully');
    }
    render() {

        return (
            <>
                <h4>Hello World</h4>

            </>
        );
    }
}

export default Child;