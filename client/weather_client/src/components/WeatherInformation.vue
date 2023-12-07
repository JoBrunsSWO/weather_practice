<template>
  <div class="container">
        <div class="inner-container">
          <h2>min {{ minTemperature }}</h2>  
          <h2>max {{ minTemperature }} °C</h2>
            <p>Relative Humidity: {{ humidity }} %</p>
            <p>Wind Speed: {{ windSpeed }} km/h</p>
            <p>{{ weatherDescription }}</p>
            <div v-if="showClear" class="weather-condition">
                <img src="../assets/0_clear.png" alt="">
            </div>
            <div v-if="showPartlyCovered" class="weather-condition">
                <img src="../assets/1_2_partly_covered.png" alt="">
            </div>
            <div v-if="showOvercast" class="weather-condition">
                <img src="../assets/3_overcast.png" alt="">
            </div>
            <div v-if="showFog" class="weather-condition">
                <img src="../assets/45_48_fog.png" alt="">
            </div>
            <div v-if="showRain" class="weather-condition">
                <img src="../assets/63_66_moderate_rain.png" alt="">
            </div>
            <div v-if="showSnow" class="weather-condition">
                <img src="../assets/71_73_75_85_86_snow_all.png" alt="">
            </div>
            <div v-if="showStorm" class="weather-condition">
                <img src="../assets/95_96_99_thunderstorm.png" alt="">
            </div>
             
            
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'WeatherInformation',
  
  data() {
    return {
      items: [],
      showClear: true
    };
  },
  async created() {
    axios.get('http://localhost:8000/api/weather/').then(
                response => {
                    console.log(response.data)
                },
  )},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    width: 100%;
    display: flex;
    justify-content: center;
}

.inner-container {
    width: 50%;
    background: rgb(158, 158, 204);

}
.weather-condition img {
    max-width: 100%;
    height: auto;
}
</style>
