package main 

import (
	"encoding/json"
	"log"
	"net/http"
	
	"github.com/gorilla/mux"
)

// contact struct (model)
type Contact struct {
	Name string 'json:"name"'
	Dog string 'json:"dog"'
}

// init contacts var as slic Contact struct
var contacts []Contact

// get all contacts 
func getContacts(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(contacts)
}

// get single contact

func main() {
	// init router 
	r := mux.NewRouter()
	
	// hardcoded data - @todo: add database
	contacts = append(contacts, contact{Name: "person", Dog: "Lab"})
	contacts = append(contacts, contact{Name: "alien", Dog: "Poodle"})
	contacts = append(contacts, contact{Name: "martian", Dog: "Irish Setter"})

	// route handles and endpoints 
	r.HandleFunc("/contacts", getContacts).Methods("GET")
	r.HandleFunc("/contacts/{name}", getContact).Methods("GET")
	r.HandleFunc("/contacts", createContact).Methods("POST")
	r.HandleFunc("/contacts/{name}", updateContact).Methods("PUT")
	r.HandleFunc("/contacts/{name}", deleteContact).Methods("DELETE")

	// start server
	log.Fatal(http.ListenAndServe(":3000", r)) 
	
}
