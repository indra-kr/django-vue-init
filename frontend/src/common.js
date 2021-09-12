import axios from 'axios'

export default {
    getDataByAxios (path, params) {
        var apiURL = path
        var rand = Math.floor(Math.random() * 10000)

        console.log('- Request: ' + rand + ') ', apiURL, ' with Params: ', params)
        return axios.get(apiURL, params)
            .then(response => {
                console.log('- (Response: ' + rand + ') ', response.data)
                return response
        })
    }
}