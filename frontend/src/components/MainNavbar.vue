<template>
    <div>
        <div class="grid grid-cols-2 px-16 mx-auto h-24 items-center">
        <img src="../assets/logo.png" alt="" class="h-16 w-28"/>
            
        <div class="flex justify-end items-center gap-8">
          <button class="text-sm font-medium">Rechercher un tournoi</button>
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
    name: "MainNavBar"
}
</script>
