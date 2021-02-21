### Airflow Cheat Sheet

```
Miscellaneous commands                                                                            
airflow cheat-sheet                       | Display cheat sheet                                   
airflow info                              | Show information about current Airflow and environment
airflow kerberos                          | Start a kerberos ticket renewer                       
airflow plugins                           | Dump information about loaded plugins                 
airflow rotate-fernet-key                 | Rotate encrypted connection credentials and variables 
airflow scheduler                         | Start a scheduler instance                            
airflow sync-perm                         | Update permissions for existing roles and DAGs        
airflow version                           | Show the version                                      
airflow webserver                         | Start a Airflow webserver instance                    
                                                                                                  
Celery components                                                            
airflow celery flower                     | Start a Celery Flower            
airflow celery stop                       | Stop the Celery worker gracefully
airflow celery worker                     | Start a Celery worker node       
                                                                             
View configuration                                                              
airflow config get-value                  | Print the value of the configuration
airflow config list                       | List options for the configuration  
                                                                                
Manage connections                                                
airflow connections add                   | Add a connection      
airflow connections delete                | Delete a connection   
airflow connections export                | Export all connections
airflow connections get                   | Get a connection      
airflow connections list                  | List connections      
                                                                  
Manage DAGs                                                                                    
airflow dags backfill                     | Run subsections of a DAG for a specified date range
airflow dags delete                       | Delete all DB records related to the specified DAG 
airflow dags list                         | List all the DAGs                                  
airflow dags list-jobs                    | List the jobs                                      
airflow dags list-runs                    | List DAG runs given a DAG id                       
airflow dags next-execution               | Get the next execution datetimes of a DAG          
airflow dags pause                        | Pause a DAG                                        
airflow dags report                       | Show DagBag loading report                         
airflow dags show                         | Displays DAG's tasks with their dependencies       
airflow dags state                        | Get the status of a dag run                        
airflow dags test                         | Execute one single DagRun                          
airflow dags trigger                      | Trigger a DAG run                                  
airflow dags unpause                      | Resume a paused DAG                                
                                                                                               
Database operations                                                                        
airflow db check                          | Check if the database can be reached           
airflow db check-migrations               | Check if migration have finished               
airflow db init                           | Initialize the metadata database               
airflow db reset                          | Burn down and rebuild the metadata database    
airflow db shell                          | Runs a shell to access the database            
airflow db upgrade                        | Upgrade the metadata database to latest version
                                                                                           
Tools to help run the KubernetesExecutor                                                                       
airflow kubernetes cleanup-pods           | Clean up Kubernetes pods in evicted/failed/succeeded states        
airflow kubernetes generate-dag-yaml      | Generate YAML files for all tasks in DAG. Useful for debugging     
                                          | tasks without launching into a cluster                             
                                                                                                               
Manage pools                                                
airflow pools delete                      | Delete pool     
airflow pools export                      | Export all pools
airflow pools get                         | Get pool size   
airflow pools import                      | Import pools    
airflow pools list                        | List pools      
airflow pools set                         | Configure pool  
                                                            
Display providers                                                                                              
airflow providers behaviours              | Get information about registered connection types with custom      
                                          | behaviours                                                         
airflow providers get                     | Get detailed information about a provider                          
airflow providers hooks                   | List registered provider hooks                                     
airflow providers links                   | List extra links registered by the providers                       
airflow providers list                    | List installed providers                                           
airflow providers widgets                 | Get information about registered connection form widgets           
                                                                                                               
Manage roles                                           
airflow roles create                      | Create role
airflow roles list                        | List roles 
                                                       
Manage tasks                                                                                  
airflow tasks clear                       | Clear a set of task instance, as if they never ran
airflow tasks failed-deps                 | Returns the unmet dependencies for a task instance
airflow tasks list                        | List the tasks within a DAG                       
airflow tasks render                      | Render a task instance's template(s)              
airflow tasks run                         | Run a single task instance                        
airflow tasks state                       | Get the status of a task instance                 
airflow tasks states-for-dag-run          | Get the status of all task instances in a dag run 
airflow tasks test                        | Test a task instance                              
                                                                                              
Manage users                                                       
airflow users add-role                    | Add role to a user     
airflow users create                      | Create a user          
airflow users delete                      | Delete a user          
airflow users export                      | Export all users       
airflow users import                      | Import users           
airflow users list                        | List users             
airflow users remove-role                 | Remove role from a user
                                                                   
Manage variables                                                
airflow variables delete                  | Delete variable     
airflow variables export                  | Export all variables
airflow variables get                     | Get variable        
airflow variables import                  | Import variables    
airflow variables list                    | List variables      
airflow variables set                     | Set variable
```