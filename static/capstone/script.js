
        // DROPDOWN MENU WITH TOGGLE ICON
        function _drop(a, b, c){
            const d = document.getElementById(a),
                  e = document.getElementById(b).getElementsByTagName('i');
            d.classList.toggle(c);
            e[0].classList.toggle('hidden');
            e[1].classList.toggle('visible')
        }
         
        // TOGGLE
        function _tgl(a, b){
            document.getElementById(a).classList.toggle(b)
        }
            
            function openSearch(){
            _drop('search', 'btnSearch', 'show-search')
        }
         
        function openMenu(){
            _drop('thisMenu', 'btnMenu', 'show-menu')
        } 
