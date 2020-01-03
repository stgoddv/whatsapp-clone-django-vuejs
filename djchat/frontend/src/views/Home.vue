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
          <div
            class="flex flex-col justify-between max-w-3xl mx-auto"
            style="min-height: 29rem;"
          >
            <div>
              <p>hola</p>
            </div>
            <div class="mb-8">
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