<template>
  <div class="tournament">
    <MainNavbar />
    <div class="featured-image">
      <img src="../assets/volleymatch.jpg" :alt="altText" class="w-full h-auto" />
    </div>
  </div>
</template>

<script>
import MainNavbar from '@/components/MainNavbar.vue';

export default {
  components: {
    MainNavbar,
  data() {
    return {
      featuredImageUrl: '../assets/volleymatch.jpg',
      altText : 'tournament title',
    }
  },
}
}
</script>
