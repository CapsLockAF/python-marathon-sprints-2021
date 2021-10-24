const howMuchSec = (...args) => {
    const [seconds=0, minutes=0, hours=0, days=0, weeks=0, months=0, years=0] = args
    return seconds 
    + (minutes*60) 
    + (hours*3600) 
    + (days*86400) 
    + (weeks*604800) 
    + (months*30*86400) 
    + (years*12*30*86400)
}
