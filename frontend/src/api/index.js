import axios from 'axios'

const API_URL = 'http://localhost:5000/api'

export function fetchTeam() {
    return axios.get(`${API_URL}/team/`)
  }
  
  export function fetchNewsFeed() {
    return axios.get(`${API_URL}/newsfeed/`)
  }