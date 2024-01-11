<template>
    <!-- Second nav bar for sports filter -->
    <div class="flex items-center justify-between space-x-5 h-20 px-16 border-b-[1px]">
        <div class="flex items-center space-x-10">
            <div @click="selectSport(null)" class="flex flex-col items-center text-gray-500 hover:text-black gap-2">
                <img src="../../assets/balls/football-ball.png" alt="" class="h-6 w-6"/>
                <p :class="{
                    'text-xs font-normal text-orange-500': !selectedSport,
                    'text-xs font-normal text-gray-500': selectedSport
                    }">Tous</p>
            </div>
            <div v-for="sport in sports" :key="sport.id" @click="selectSport(sport.id)" class="flex flex-col items-center text-gray-500 hover:text-black gap-2">
                <img src="../../assets/balls/football-ball.png" alt="" class="h-6 w-6"/>
                <p :class="{
                    'text-xs font-normal text-orange-500': selectedSport === sport.id,
                    'text-xs font-normal text-gray-500': selectedSport !== sport.id
                    }">{{ sport.name }}</p>
            </div>

        </div>
    </div>
</template>

<script>

export default {
    name: 'SecondNavbar',
    
    props: {
        sports: {
            type: Array,
            required: true,
        },
        changeSelectedSport: {
            type: Function,
            required: true,
        },
    },

    data() {
        return {
            selectedSport: null
        }
        
    },

    methods: {
        selectSport(sportId) {
        this.selectedSport = sportId;
        this.changeSelectedSport(this.selectedSport);
        },
  },
   
};

</script>
