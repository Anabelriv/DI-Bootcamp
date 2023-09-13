const Parent = (props) => {
    console.log("props=>", props)
    if (props.user === 'admin') {
        return (<>
            <h1>Admin Dashboard</h1>
        </>)
    }
    return props.children;
}

export default Parent