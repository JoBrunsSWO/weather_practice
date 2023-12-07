<template>
    <h1>Weather Information for Berlin</h1>
    <div class="container">
        <div class="current-container">
            <h2>Current Weather</h2>
            <p>Time: {{ time }}</p>
            <p>Temperature: {{ currentTemperature }} °C</p>
            <p>Relative Humidity: {{ currentHumidity }} %</p>
            <p>Wind Speed: {{ currentWindSpeed }} km/h</p>
            
            
            <p>{{ currentDescription }}</p>
            <div v-if="currentDescription === 'Clear'" class="weather-condition">
                <img src="../assets/0_clear.png" alt="">
            </div>
            <div v-if="currentDescription === 'Partly Covered'" class="weather-condition">
                <img src="../assets/1_2_partly_covered.png" alt="">
            </div>
            <div v-if="currentDescription === 'Overcast'" class="weather-condition">
                <img src="../assets/3_overcast.png" alt="">
            </div>
            <div v-if="currentDescription === 'Fog'" class="weather-condition">
                <img src="../assets/45_48_fog.png" alt="">
            </div>
            <div v-if="currentDescription === 'Rain'" class="weather-condition">
                <img src="../assets/63_66_moderate_rain.png" alt="">
            </div>
            <div v-if="currentDescription === 'Snow'" class="weather-condition">
                <img src="../assets/71_73_75_85_86_snow_all.png" alt="">
            </div>
            <div v-if="currentDescription === 'Storm'" class="weather-condition">
                <img src="../assets/95_96_99_thunderstorm.png" alt="">
            </div>
        </div>
        <div class="daily-container">
            <div class="day-container" v-for="(dayTime, index) in dailyTime" :key="index">
                <div class="image-container">
                    <div v-if="dailyDescription[index] === 'Clear'" class="daily-weather-condition">
                        <img src="../assets/0_clear.png" alt="">
                    </div>
                    <div v-if="dailyDescription[index] === 'Partly Covered'" class="daily-weather-condition">
                        <img src="../assets/1_2_partly_covered.png" alt="">
                    </div>
                    <div v-if="dailyDescription[index] === 'Overcast'" class="daily-weather-condition">
                        <img src="../assets/3_overcast.png" alt="">
                    </div>
                    <div v-if="dailyDescription[index] === 'Fog'" class="daily-weather-condition">
                        <img src="../assets/45_48_fog.png" alt="">
                    </div>
                    <div v-if="dailyDescription[index] === 'Rain'" class="daily-weather-condition">
                        <img src="../assets/63_66_moderate_rain.png" alt="">
                    </div>
                    <div v-if="dailyDescription[index] === 'Snow'" class="daily-weather-condition">
                        <img src="../assets/71_73_75_85_86_snow_all.png" alt="">
                    </div>
                    <div v-if="dailyDescription[index] === 'Storm'" class="daily-weather-condition">
                        <img src="../assets/95_96_99_thunderstorm.png" alt="">
                    </div>  
                </div>
                <div class="data-container-1">
                    <p><b v-if="index===0">Today, </b><b v-if="index===1">Tomorrow, </b>{{ dayTime }}</p>
                    <p>min. Temperature {{ dailyMinTemperature[index] }} °C</p>
                    <p>max. Temperature {{ dailyMaxTemperature[index] }} °C</p>
                </div>  
                <div class="data-container-2">
                    <p>Precipitation {{ dailyPrecipitationSum[index] }} mm</p>
                    <p>Precipitation Probability {{ dailyPrecipitationProbability[index] }} %</p>
                    <p>Wind Speed {{ dailyWindSpeed[index] }} km/h</p>
                </div>
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
      time: '',

      currentTemperature: '',
      currentHumidity: '',
      currentWindSpeed: '',
      currentDescription: '',


      dailyTime: [],
      dailyWeatherCode: [],
      dailyMinTemperature: [],
      dailyMaxTemperature: [],
      dailyPrecipitationSum: [],
      dailyPrecipitationProbability: [],
      dailyWindSpeed: [],
      dailyDescription: []
      
    };
  },
  methods: {
    assignDescription(code) {
        switch(code) {
            case 0:
                return 'Clear';
            case 1:
            case 2:
                return 'Partly covered';
            case 3:
                return 'Overcast';
            case 45:
            case 48:
                return 'Fog';
            case 51:
            case 52:
            case 55:
            case 56:
            case 57:
            case 61:
            case 63:
            case 65:
            case 66:
            case 67:
            case 80:
            case 81:
            case 82:
                return 'Rain';
            case 71:
            case 73:
            case 75:
            case 77:
            case 85:
            case 86:
                return 'Snow';
            case 95:
            case 96:
            case 99:
                return 'Storm';
        }
    }
  },
  async created() {
    axios.get('http://localhost:8000/api/weather/').then(
                response => {
                    this.currentDescription = this.assignDescription(response.data.current_weather_code);
                    this.time = response.data.current_time;
                    this.currentTemperature = response.data.current_temperature_2m;
                    this.currentHumidity = response.data.current_humidity_2m;
                    this.currentWindSpeed = response.data.current_wind_speed_10m;
                    this.dailyTime = response.data.daily_time;
                    this.dailyWeatherCode = response.data.daily_weather_code;
                    this.dailyMinTemperature = response.data.daily_temperature_2m_min;
                    this.dailyMaxTemperature = response.data.daily_temperature_2m_max;
                    this.dailyPrecipitationSum = response.data.daily_precipitation_sum;
                    this.dailyPrecipitationProbability = response.data.daily_precipitation_probability;
                    this.dailyWindSpeed = response.data.daily_wind_speed_10m_max;
                    console.log(this.dailyWeatherCode)
                    for (let i = 0; i < this.dailyWeatherCode.length; i++) {
                        this.dailyDescription.push(this.assignDescription(this.dailyWeatherCode[i]));
                    }      
                }).catch(error => {
                    console.log(error);
                });

                
    },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
    margin: 0.25rem;
}
.container {
    width: 100%;
    display: flex;
    justify-content: center;
}

.current-container {
    width: 50%;
    background: rgb(158, 158, 204);

}
.weather-condition img {
    max-width: 100%;
    height: auto;
}

.daily-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}
.day-container {
    background:rgb(158, 158, 204);
    margin: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-align: start;
}

.image-container {
    max-width: 20%;
}
.daily-weather-condition img {
    max-width: 50%;
    width: auto;
}
</style>
