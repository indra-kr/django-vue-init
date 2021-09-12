<template>
  <div id="app">
    <h1>{{ data }}</h1>
  </div>
</template>

<script>
import common from '../src/common'

export default {
  name: 'App',
  components: {
  },
  data () {
    return {
      data: null
    }
  },
  created () {
    common.getDataByAxios('/api/v1/apidemo', null)
      .then(response => {
        this.data = response.data
      })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
