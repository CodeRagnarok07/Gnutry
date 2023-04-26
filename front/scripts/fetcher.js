const fetcher = async (path, method) => {
    try {
        const resApi = await fetch(path, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
        })
        const dataApi = await resApi.json()
        return dataApi
    } catch (error) {
        console.log("network error", error)
        console.log("FAIL FETCH TO PATH", path);
        return { data: error }
    }
}

export default fetcher