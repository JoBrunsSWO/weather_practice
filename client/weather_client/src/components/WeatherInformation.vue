<template>
    <h1>Weather Information for Berlin</h1>
    <div class="container">
        <div class="current-container">
            <h2>Weather on {{ time }}</h2>
            <p>{{ currentDescription }}</p>
            <br>
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
            <div class="current-data-container">
                <p><svg xmlns="http://www.w3.org/2000/svg" height="16" width="10" viewBox="0 0 320 512"><path d="M160 64c-26.5 0-48 21.5-48 48V276.5c0 17.3-7.1 31.9-15.3 42.5C86.2 332.6 80 349.5 80 368c0 44.2 35.8 80 80 80s80-35.8 80-80c0-18.5-6.2-35.4-16.7-48.9c-8.2-10.6-15.3-25.2-15.3-42.5V112c0-26.5-21.5-48-48-48zM48 112C48 50.2 98.1 0 160 0s112 50.1 112 112V276.5c0 .1 .1 .3 .2 .6c.2 .6 .8 1.6 1.7 2.8c18.9 24.4 30.1 55 30.1 88.1c0 79.5-64.5 144-144 144S16 447.5 16 368c0-33.2 11.2-63.8 30.1-88.1c.9-1.2 1.5-2.2 1.7-2.8c.1-.3 .2-.5 .2-.6V112zM208 368c0 26.5-21.5 48-48 48s-48-21.5-48-48c0-20.9 13.4-38.7 32-45.3V208c0-8.8 7.2-16 16-16s16 7.2 16 16V322.7c18.6 6.6 32 24.4 32 45.3z"/></svg> 
                 {{ currentTemperature }} °C</p>
            <p><svg xmlns="http://www.w3.org/2000/svg" height="16" width="18" viewBox="0 0 576 512"><path d="M269.5 69.9c11.1-7.9 25.9-7.9 37 0C329 85.4 356.5 96 384 96c26.9 0 55.4-10.8 77.4-26.1l0 0c11.9-8.5 28.1-7.8 39.2 1.7c14.4 11.9 32.5 21 50.6 25.2c17.2 4 27.9 21.2 23.9 38.4s-21.2 27.9-38.4 23.9c-24.5-5.7-44.9-16.5-58.2-25C449.5 149.7 417 160 384 160c-31.9 0-60.6-9.9-80.4-18.9c-5.8-2.7-11.1-5.3-15.6-7.7c-4.5 2.4-9.7 5.1-15.6 7.7c-19.8 9-48.5 18.9-80.4 18.9c-33 0-65.5-10.3-94.5-25.8c-13.4 8.4-33.7 19.3-58.2 25c-17.2 4-34.4-6.7-38.4-23.9s6.7-34.4 23.9-38.4C42.8 92.6 61 83.5 75.3 71.6c11.1-9.5 27.3-10.1 39.2-1.7l0 0C136.7 85.2 165.1 96 192 96c27.5 0 55-10.6 77.5-26.1zm37 288C329 373.4 356.5 384 384 384c26.9 0 55.4-10.8 77.4-26.1l0 0c11.9-8.5 28.1-7.8 39.2 1.7c14.4 11.9 32.5 21 50.6 25.2c17.2 4 27.9 21.2 23.9 38.4s-21.2 27.9-38.4 23.9c-24.5-5.7-44.9-16.5-58.2-25C449.5 437.7 417 448 384 448c-31.9 0-60.6-9.9-80.4-18.9c-5.8-2.7-11.1-5.3-15.6-7.7c-4.5 2.4-9.7 5.1-15.6 7.7c-19.8 9-48.5 18.9-80.4 18.9c-33 0-65.5-10.3-94.5-25.8c-13.4 8.4-33.7 19.3-58.2 25c-17.2 4-34.4-6.7-38.4-23.9s6.7-34.4 23.9-38.4c18.1-4.2 36.2-13.3 50.6-25.2c11.1-9.4 27.3-10.1 39.2-1.7l0 0C136.7 373.2 165.1 384 192 384c27.5 0 55-10.6 77.5-26.1c11.1-7.9 25.9-7.9 37 0zm0-144C329 229.4 356.5 240 384 240c26.9 0 55.4-10.8 77.4-26.1l0 0c11.9-8.5 28.1-7.8 39.2 1.7c14.4 11.9 32.5 21 50.6 25.2c17.2 4 27.9 21.2 23.9 38.4s-21.2 27.9-38.4 23.9c-24.5-5.7-44.9-16.5-58.2-25C449.5 293.7 417 304 384 304c-31.9 0-60.6-9.9-80.4-18.9c-5.8-2.7-11.1-5.3-15.6-7.7c-4.5 2.4-9.7 5.1-15.6 7.7c-19.8 9-48.5 18.9-80.4 18.9c-33 0-65.5-10.3-94.5-25.8c-13.4 8.4-33.7 19.3-58.2 25c-17.2 4-34.4-6.7-38.4-23.9s6.7-34.4 23.9-38.4c18.1-4.2 36.2-13.3 50.6-25.2c11.1-9.5 27.3-10.1 39.2-1.7l0 0C136.7 229.2 165.1 240 192 240c27.5 0 55-10.6 77.5-26.1c11.1-7.9 25.9-7.9 37 0z"/></svg>
                 {{ currentHumidity }} %</p>
            <p><svg xmlns="http://www.w3.org/2000/svg" height="16" width="16" viewBox="0 0 512 512"><path d="M288 32c0 17.7 14.3 32 32 32h32c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32 14.3-32 32s14.3 32 32 32H352c53 0 96-43 96-96s-43-96-96-96H320c-17.7 0-32 14.3-32 32zm64 352c0 17.7 14.3 32 32 32h32c53 0 96-43 96-96s-43-96-96-96H32c-17.7 0-32 14.3-32 32s14.3 32 32 32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H384c-17.7 0-32 14.3-32 32zM128 512h32c53 0 96-43 96-96s-43-96-96-96H32c-17.7 0-32 14.3-32 32s14.3 32 32 32H160c17.7 0 32 14.3 32 32s-14.3 32-32 32H128c-17.7 0-32 14.3-32 32s14.3 32 32 32z"/></svg> 
                 {{ currentWindSpeed }} km/h
            </p>
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
                <div class="data-container-overview">
                    <p>
                        <b v-if="index===0">Today, </b><b v-if="index===1">Tomorrow, </b><b>{{ dayTime }}</b>
                    </p>
                    <p>
                        {{ dailyDescription[index] }}
                    </p>
                </div>
                <div class="data-container-temp-wind">
                    <p>
                        <svg xmlns="http://www.w3.org/2000/svg" height="16" width="10" viewBox="0 0 320 512"><path d="M160 64c-26.5 0-48 21.5-48 48V276.5c0 17.3-7.1 31.9-15.3 42.5C86.2 332.6 80 349.5 80 368c0 44.2 35.8 80 80 80s80-35.8 80-80c0-18.5-6.2-35.4-16.7-48.9c-8.2-10.6-15.3-25.2-15.3-42.5V112c0-26.5-21.5-48-48-48zM48 112C48 50.2 98.1 0 160 0s112 50.1 112 112V276.5c0 .1 .1 .3 .2 .6c.2 .6 .8 1.6 1.7 2.8c18.9 24.4 30.1 55 30.1 88.1c0 79.5-64.5 144-144 144S16 447.5 16 368c0-33.2 11.2-63.8 30.1-88.1c.9-1.2 1.5-2.2 1.7-2.8c.1-.3 .2-.5 .2-.6V112zM208 368c0 26.5-21.5 48-48 48s-48-21.5-48-48c0-20.9 13.4-38.7 32-45.3V208c0-8.8 7.2-16 16-16s16 7.2 16 16V322.7c18.6 6.6 32 24.4 32 45.3z"/></svg> 
                         {{ dailyMinTemperature[index] }} - {{ dailyMaxTemperature[index] }}°C
                    </p>
                    <p>
                        <svg xmlns="http://www.w3.org/2000/svg" height="16" width="16" viewBox="0 0 512 512"><path d="M288 32c0 17.7 14.3 32 32 32h32c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32 14.3-32 32s14.3 32 32 32H352c53 0 96-43 96-96s-43-96-96-96H320c-17.7 0-32 14.3-32 32zm64 352c0 17.7 14.3 32 32 32h32c53 0 96-43 96-96s-43-96-96-96H32c-17.7 0-32 14.3-32 32s14.3 32 32 32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H384c-17.7 0-32 14.3-32 32zM128 512h32c53 0 96-43 96-96s-43-96-96-96H32c-17.7 0-32 14.3-32 32s14.3 32 32 32H160c17.7 0 32 14.3 32 32s-14.3 32-32 32H128c-17.7 0-32 14.3-32 32s14.3 32 32 32z"/></svg>
                         {{ dailyWindSpeed[index] }} km/h
                    </p>
                </div>  
                <div class="data-container-precipitation">
                    <p>
                        <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512"><path d="M192 512C86 512 0 426 0 320C0 228.8 130.2 57.7 166.6 11.7C172.6 4.2 181.5 0 191.1 0h1.8c9.6 0 18.5 4.2 24.5 11.7C253.8 57.7 384 228.8 384 320c0 106-86 192-192 192zM96 336c0-8.8-7.2-16-16-16s-16 7.2-16 16c0 61.9 50.1 112 112 112c8.8 0 16-7.2 16-16s-7.2-16-16-16c-44.2 0-80-35.8-80-80z"/></svg>
                         {{ dailyPrecipitationSum[index] }} mm
                    </p>
                    <p>
                        <svg xmlns="http://www.w3.org/2000/svg" height="16" width="18" viewBox="0 0 576 512"><path d="M288 0c17.7 0 32 14.3 32 32V49.7C451.8 63.4 557.7 161 573.9 285.9c2 15.6-17.3 24.4-27.8 12.7C532.1 283 504.8 272 480 272c-38.7 0-71 27.5-78.4 64.1c-1.7 8.7-8.7 15.9-17.6 15.9s-15.8-7.2-17.6-15.9C359 299.5 326.7 272 288 272s-71 27.5-78.4 64.1c-1.7 8.7-8.7 15.9-17.6 15.9s-15.8-7.2-17.6-15.9C167 299.5 134.7 272 96 272c-24.8 0-52.1 11-66.1 26.7C19.4 310.4 .1 301.5 2.1 285.9C18.3 161 124.2 63.4 256 49.7V32c0-17.7 14.3-32 32-32zm0 304c12.3 0 23.5 4.6 32 12.2V430.6c0 45-36.5 81.4-81.4 81.4c-30.8 0-59-17.4-72.8-45l-2.3-4.7c-7.9-15.8-1.5-35 14.3-42.9s35-1.5 42.9 14.3l2.3 4.7c3 5.9 9 9.6 15.6 9.6c9.6 0 17.4-7.8 17.4-17.4V316.2c8.5-7.6 19.7-12.2 32-12.2z"/></svg>
                         {{ dailyPrecipitationProbability[index] }} %
                    </p>
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
        // initialize all variables
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
        // assign description to every possible weather code
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
                    // assign response data to variables
                    this.currentDescription = this.assignDescription(response.data.current_weather_code); // assign description to current weather code
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
                        // assign description to the daily weather codes
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
    max-width: 70%;
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
    margin: 0.125rem 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-align: start;
}

.image-container {
    max-width: 10%;
}

.daily-weather-condition img {
    max-width: 80%;
    width: auto;
}

.data-container-overview {
    width: 30%;
}

.data-container-temp-wind {
    width: 20%;
}

.data-container-precipitation {
    width: 20%;
}

.current-data-container {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
}
</style>
