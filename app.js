const Getdata = async()=>{
    const url = 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=npbhzl4zYFre5nK6tCfwCFq4MwVe8KDA'
    const resp = await fetch(url)
    const {location} = await resp.json()
    const {lat,lon} = location
    console.log(`La latitud es ${lat} y la longuitud es ${lon}`)
}
Getdata()