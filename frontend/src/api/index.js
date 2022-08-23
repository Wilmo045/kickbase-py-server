import axios from 'axios'

const API_URL = 'http://localhost:5000/api'

export function login(username, password) {
  return axios.post(`${API_URL}/auth/login`, username, password)
}

export function fetchTeam(leagueId) {
  return axios.get(`${API_URL}/league/${leagueId}/userplayers`)
}

export function fetchNewsFeed() {
  return axios.get(`${API_URL}/newsfeed/`)
}