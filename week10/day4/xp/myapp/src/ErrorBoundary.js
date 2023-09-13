import React from "react";

class ErrorBoundary extends React.Component {
    constructor() {
        super()
        this.state = {
            hasError: false,
            error: "",
            errorInfo: ""
        }
    }
    componentDidCatch = (error, errorinfo) => {
        this.setState({ hasError: true, error: error, errorInfo: errorinfo });

    }
    render() {
        console.log(this.state);

        if (this.state.hasError) {
            return (
                <details style={{ whiteSpace: 'pre-wrap' }}>
                    {this.state.error && this.state.error.toString()}
                    <br />
                    {this.state.errorInfo.componentStack}
                </details>)
        }
        return this.props.children;
    }
}


export default ErrorBoundary;