<template>
  <div class="gmp-GoogleMap"></div>
</template>

<script>
  import style from './style.js'

  export default {
    data () {
      return {
        'position': undefined,
        'map': undefined,
        'marker': undefined
      }
    },
    props: ['lat', 'lng', 'location', 'zoom'],
    mounted () {
      if (this.lat && this.lng) {
        this.position = new google.maps.LatLng(this.lat, this.lng)
        this.plotMap()
      } else if (this.location) {
        const geocoder = new google.maps.Geocoder()
        geocoder.geocode({'address': this.location}, (results, status) => {
          if (status === 'OK') {
            this.position = results[0].geometry.location
            this.plotMap()
          }
        })
      }
    },
    methods: {
      plotMap () {
        this.map = new google.maps.Map(this.$el, {
          center: this.position,
          zoom: this.zoom ? parseInt(this.zoom, 11) : 11,
          disableDefaultUI: true,
          styles: style,
          scrollwheel: true
        })
        this.marker = new google.maps.Marker({
          position: this.position,
          map: this.map
        })
      }
    }
  }
</script>
