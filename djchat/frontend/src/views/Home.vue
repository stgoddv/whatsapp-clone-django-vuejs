<template>
  <div class="home">

    <div class="flex flex-wrap mt-5">

      <div class="w-3/12 p-3">
        <p class="text-2xl my-4">Whatsapp Clone</p>

        <div
          class="shadow-md border rounded-lg"
          style="min-height: 12rem;"
        >
        </div>

        <div
          class="shadow-md border rounded-lg"
          style="min-height: 12rem; margin-top: 1rem;"
        >
        </div>
      </div>

      <div class="w-9/12 p-3">
        <div class="shadow-md border rounded-lg">
          <div class="flex flex-col justify-between mx-8">
            <div class="mt-8">
              <div
                class="border rounded-lg border-teal-500 py-2 chat"
                style="min-height: 20rem;"
              >
                <div class="max-w-lg">
                  <div class="shadow border rounded-lg m-5 px-4 relative bg-white">

                    <div class="flex justify-between py-1 mt-1">
                      <p class="text-xs text-purple-600 font-bold">stgoddv@gmail.com</p>
                      <p class="text-xs text-gray-600">~Santiago</p>
                    </div>

                    <div class="mb-3">
                      <p class="text-left">buena cabros eso es lo que está pasando con la volá y la onda del asado.</p>
                    </div>

                    <div
                      class="absolute"
                      style="right: 10px; bottom: 5px;"
                    >
                      <p class="text-xs text-gray-600">16:42</p>
                    </div>

                  </div>
                </div>

                <div class="max-w-lg ml-auto">
                  <div class="shadow border rounded-lg m-5 px-4 relative bg-green-200">

                    <div class="mb-3 mt-2">
                      <p class="text-left">buena cabros eso es lo que está pasando con la volá y la onda del asado.</p>
                    </div>

                    <div
                      class="absolute"
                      style="right: 10px; bottom: 5px;"
                    >
                      <p class="text-xs text-gray-600">16:42</p>
                    </div>

                  </div>
                </div>

              </div>
            </div>
            <div class="mt-5">
              <div class="flex items-center border rounded-lg border-teal-500 py-2">
                <input
                  class="ml-3 text-lg appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                  type="text"
                  placeholder="Send a message"
                  aria-label="Enter text"
                >
                <button
                  class="mr-3 flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                  type="button"
                  style="transition: background-color 0.3s;"
                >
                  <send-icon
                    size="1.5x"
                    class="custom-class inline-block"
                  ></send-icon>
                  <p class="inline-block mx-3 text-lg">Enviar</p>
                </button>
              </div>

            </div>
            <div class="my-1 text-right">
              <a
                style="font-size: 9px;"
                href="http://www.freepik.com"
              >Background vector created by kjpargeter - www.freepik.com</a>
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
import { SendIcon } from "vue-feather-icons";

export default {
  components: {
    SendIcon
  }
};
</script>

<style scoped>
.chat {
  position: relative;
}
.chat::after {
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  content: "";
  opacity: 0.5;
  position: absolute;
  background-image: url("~@/assets/imgs/main-bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  z-index: -1;
}
</style>