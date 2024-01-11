<template>
  <div class="">
  <Navbar 
    :cities="cities"
    :levels="levels" 
    :selectedCity="selectedCity" 
    :selectedLevel="selectedLevel" 
    :selectedStartDate="selectedStartDate" 
    :selectedEndDate="selectedEndDate"
    @search="performSearch"/>

  <SecondNavbar :selectedSport="selectedSport" :sports="sports" :changeSelectedSport="changeSelectedSport" />
  <Map :tournaments="filteredTournaments" />
  
</div>
</template>

<script>
import axios from "axios";

import Navbar from '../components/navbars/Navbar.vue';
import SecondNavbar from '../components/navbars/SecondNavbar.vue';
import Map from '../components/Map.vue';

export default {
  components: {
    Navbar,
    SecondNavbar,
    Map,
  },

  data() {
    return {
      //Tournaments:
      tournaments: [],
      filteredTournaments: [],

      //all existing filters:
      cities: [],
      sports: [],
      levels: [], 
      
      // Filtered tournaments based on user selection
      selectedCity: null,
      selectedSport: null,
      selectedLevel: null,
      selectedStartDate: '',
      selectedEndDate: '',
    }
  },

  methods: {
    async fetchTournamentList() {
            try {
                const response = await axios.get('http://localhost:8000/api/tournament/');
                this.tournaments = response.data;
                if (this.tournaments.length > 0) {
                this.tournaments.forEach((tournament) => {
                    tournament.coords = [tournament.locationLat, tournament.locationLon];
                });
                }
                this.filteredTournaments = this.tournaments
            } catch (error) {
                console.error("Error fetching tournament list:", error);
            }
        },
    async fetchSportList() {
      try {
          const response = await axios.get('http://localhost:8000/api/sport/');
          this.sports = response.data;
      } catch (error) {
          console.error("Error fetching sport list:", error);
      }
    },
    async fetchCityList() {
            try {
                const response = await axios.get('http://localhost:8000/api/city/');
                this.cities = response.data;
            } catch (error) {
                console.error("Error fetching city list:", error);
            }
        },
    async fetchLevelList() {
        try {
            const response = await axios.get('http://localhost:8000/api/level/');
            this.levels = response.data;
        } catch (error) {
            console.error("Error fetching level list:", error);
        }
    },

    mainFilterTournaments() {
      this.filteredTournaments = this.tournaments.filter(tournament => 
          (!this.selectedSport || tournament.sport === this.selectedSport) &&
          (!this.selectedCity || tournament.city === this.selectedCity) &&
          (!this.selectedLevel || tournament.level.includes(this.selectedLevel)) &&
          (!this.selectedStartDate || tournament.date >= this.selectedStartDate) &&
          (!this.selectedEndDate || tournament.date <= this.selectedEndDate)
      );
    },
    
    performSearch({ selectedCity, selectedLevel, selectedStartDate, selectedEndDate }) {
      // Update data properties with the new filters
      this.selectedCity = selectedCity;
      this.selectedLevel = selectedLevel;
      this.selectedStartDate = selectedStartDate;
      this.selectedEndDate = selectedEndDate;

      // Implement your tournament filtering logic based on the new filters
      this.mainFilterTournaments()
    },

    changeSelectedSport (newSelectedSport) {
      this.selectedSport = newSelectedSport;
      this.mainFilterTournaments()
    }
  },

  mounted() {
      // Fetch your tournaments data from the API and update the 'tournaments' array
      this.fetchTournamentList(),
      this.fetchCityList(),
      this.fetchSportList(),
      this.fetchLevelList()
    },
}
</script>
