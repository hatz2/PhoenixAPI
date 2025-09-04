protoc `
  --doc_out=./docs `
  --doc_opt=markdown,api.md `
(Get-ChildItem "phoenixapi/protos/**/*.proto").FullName.Substring((Resolve-Path ".").Path.Length + 1) `
  "phoenixapi/protos/*.proto"

protoc `
  --doc_out=./docs `
  --doc_opt=html,index.html `
(Get-ChildItem "phoenixapi/protos/**/*.proto").FullName.Substring((Resolve-Path ".").Path.Length + 1) `
  "phoenixapi/protos/*.proto"
