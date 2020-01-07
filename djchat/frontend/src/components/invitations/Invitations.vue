<template>
  <div class="invitations-tabs">
    <div
      class="shadow-md border rounded-lg bg-white mt-3 relative"
      style="height: 15rem;"
    >

      <!-- Selection Tabs -->
      <div class="tabs-selection bg-white">
        <nav class="flex flex-wrap px-1">
          <button
            @click="selectedTab = 0"
            class="w-1/2 text-gray-600 py-3 block hover:text-blue-500 focus:outline-none"
            :class="{ 'text-blue-500 border-b-2 font-medium border-blue-500': selectedTab === 0 }"
          >
            Sent
          </button>
          <button
            @click="selectedTab = 1"
            class="w-1/2 text-gray-600 py-3 block hover:text-blue-500 focus:outline-none"
            :class="{ 'text-blue-500 border-b-2 font-medium border-blue-500': selectedTab === 1 }"
          >
            Received
          </button>
        </nav>
      </div>

      <!-- Tabs Content -->
      <div class="tabs-content">

        <!-- Sent Tab -->
        <div v-if="selectedTab === 0">

          <p class="text-sm mt-8">Say hello to a friend!</p>

          <button
            class="absolute py-2 px-4 shadow-md no-underline 
          rounded-full bg-blue-500 text-white font-sans font-semibold 
          text-sm border-blue-500 btn-primary hover:text-white 
          hover:bg-blue-400 focus:outline-none 
          active:shadow-none mr-2"
            style="top: 55%; 
            -ms-transform: translateY(-50%); transform: translateY(-50%);
            -ms-transform: translateX(-50%); transform: translateX(-50%);"
          >
            Invite a Friend</button>

        </div>

        <!-- Received Tab -->
        <div v-else>
          <p class="text-sm mt-8">You have not received any invitation yet</p>

          <button
            class="absolute py-2 px-4 shadow-md no-underline 
          rounded-full bg-blue-500 text-white font-sans font-semibold 
          text-sm border-blue-500 btn-primary hover:text-white 
          hover:bg-blue-400 focus:outline-none 
          active:shadow-none mr-2"
            style="top: 55%; 
            -ms-transform: translateY(-50%); transform: translateY(-50%);
            -ms-transform: translateX(-50%); transform: translateX(-50%);"
          >
            Invite a Friend</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedTab: 0
    };
  }
};
</script>