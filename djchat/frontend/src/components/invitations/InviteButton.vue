<template>
  <button
    @click="$emit('action')"
    class="py-2 px-4 shadow-md no-underline 
          rounded-full bg-blue-500 text-white font-sans font-semibold 
          text-sm border-blue-500 btn-primary hover:text-white 
          hover:bg-blue-400 focus:outline-none 
          active:shadow-none mr-2"
  >
    Invite a Friend
  </button>
</template>
