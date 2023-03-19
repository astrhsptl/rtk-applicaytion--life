import axios from "axios";

export default async function getActivities(link, setter) {
    let request = await axios.get(link);
    let data = await request.data;
    await setter(data)
    await console.log(data)
  };