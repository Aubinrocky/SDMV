<template>
    <div>
    <!-- Main navbar -->
    <div class="grid grid-cols-3 px-16 mx-auto h-24 items-center">
        <img src="../../assets/logo.png" alt="" class="h-16 w-28"/>
            <form @submit.prevent="search" class="flex justify-evenly items-center rounded-full h-12 space-x-1">

                <!-- City filter -->
                <div v-if="cities.length" class="relative">
                    <span class="text-sm">Où ?</span>
                    <select v-model="localSelectedCity" id="city" class="rounded-full py-2 px-4 border border-gray-300 outline-none">
                    <option value="">-</option>
                    <option v-for="city in cities" :key="city.id" :value="city.id">{{ city.name }}</option>
                    </select>
                </div>
                
                <!-- Level filter -->
                <div v-if="levels.length" class="relative">
                    <span class="text-sm">À quel niveau ?</span>
                    <select v-model="localSelectedLevel" id="level" class="rounded-full py-2 px-4 border border-gray-300 outline-none">
                    <option value="" selected>-</option>
                    <option v-for="level in levels" :key="level.id" :value="level.id">{{ level.name }}</option>
                    </select>
                </div>

                <!-- Date range filter -->
                <div class="relative">
                    <span class="text-sm">De quand ?</span>
                    <input v-model="localSelectedStartDate" type="date" id="startDate" class="rounded-full py-2 px-4 border border-gray-300 outline-none ">
                </div>
                <div class="relative">
                    <span class="text-sm">À quand ?</span>
                    <input v-model="localSelectedEndDate" type="date" id="endDate" class="rounded-full py-2 px-4 border border-gray-300 outline-none ">
                </div>

                <!-- Search button -->
                <div class="relative">
                    <span class="text-white">.</span>
                    <button type="submit" class="rounded-full bg-orange-500 text-white px-4 py-2"><font-awesome-icon icon="search" /></button>
                </div>
                
            </form>
            
        <div class="flex justify-end items-center gap-8">
            <button class="text-sm font-medium">Ajouter un tournoi</button>
            <div class="flex justify-evenly items-center gap-2 rounded-full border shadow-md h-10 w-20 py-1.25 pr-1.25 pl-3">
                <i><font-awesome-icon icon="bars" /></i>
                <button class="bg-black text-white rounded-full text-center w-7 h-7 text-[10px] font-semibold">E</button>
            </div>
        </div>
    </div>  
    <div class="border-b-[1px]"></div>
</div>     
</template>

<script>

export default {
    name: "Navbar",
    
    props: {
        cities: {
        type: Array,
        required: true,
        },
        levels: {
        type: Array,
        required: true,
        },
        selectedCity: {
        type: Number,
        },
        selectedLevel: {
        type: Number,
        },
        selectedStartDate: {
        type: String,
        },
        selectedEndDate: {
        type: String,
        },
    },

    data() {
        return {
            localSelectedCity: this.selectedCity || null,
            localSelectedLevel: this.selectedLevel || null,
            localSelectedStartDate: this.selectedStartDate || "",
            localSelectedEndDate: this.selectedEndDate || "",
        }
    },

    methods: {

        search() {
            // Emit an event to notify the parent component (Home.vue) about the search criteria changes
            this.$emit("search", {
                selectedCity: this.localSelectedCity === "" ? null : parseInt(this.localSelectedCity),
                selectedLevel: this.localSelectedLevel === "" ? null : parseInt(this.localSelectedLevel),
                selectedStartDate: this.localSelectedStartDate,
                selectedEndDate: this.localSelectedEndDate,
        });
    },
        

    },
};
</script>
